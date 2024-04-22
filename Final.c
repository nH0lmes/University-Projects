#include <stdio.h>
#include <math.h>
#define PI 3.14159265359

typedef struct {            //struct to be used for complex numbers
    double real;
    double imag;
} Complex;


double mag(Complex comp){                           //function to return the magnitude of a complex number, used later in the code
    return sqrt(pow(comp.real,2)+pow(comp.imag,2));
}


int isequal(Complex num1,Complex num2){             // Compares 2 complex numbers and returns 1(true) if the are equal or 0 (false) if not
    return (num1.real == num2.real && num1.imag == num2.imag);
}


void h1(int N,double T, Complex *h1_result){        //Function for h1. Returns nothing but has a pointer to an array.
    for (int k=0;k<N;k++){                          //I used an array here so that it was in the same format as h3 and the dft/ift could be done easier
        double tk = k*T/N;                          //Loops through N values and stores the real and imaginary parts to the array
        h1_result[k].real = cos(tk) + cos(5*tk);
        h1_result[k].imag = sin(tk) + sin(5*tk);
    }
}


void h2(int N,double T, Complex *h2_result){        //Function for h2, identical to h1 excpet for the mathematical function.
    for (int k=0;k<N;k++){
        double tk = k*T/N;
        h2_result[k].real = exp(pow(tk-PI,2)/2);
        h2_result[k].imag = 0;
    }
}


void h3(Complex *h3_data){                          //Function for h3. Reads values from the text file and saves them to an array.
    FILE *h3;                                       // Also takes a pointer to an array as an argument
    int num;
    double t,real,imag;
    h3 = fopen("h3.txt","r+");
    if (h3 == NULL){
        printf("ERROR\n");
        return;
    }
    for (int n=0; n<200 ;n++){                              //loops through each row in the txt file and saves the real and imaginary values to the array
        fscanf(h3,"%d, %lf, %lf, %lf",&num,&t,&real,&imag);
        h3_data[n].real = real;
        h3_data[n].imag = imag;
    }
    fclose(h3);
}


Complex dft(int num,int N, int n, double T){                    //Discrete fourier transform function
    Complex series[N];                                          //Loads in the desired array depending the inputted function; h1,h2 or h3
    Complex dft_result = {0.0,0.0};                             
    if (num==1){                                                
        h1(N,T,series);
    }
    else if (num==2){
        h2(N,T,series);
    }
    else if (num==3){
        h3(series);
    }    

    for (int k = 0; k < N; k++) {                               //Performs the discrete fourier transform calculation
        double tk = k * T / N;
        dft_result.real += (series[k].real * cos(n * tk) + series[k].imag * sin(n * tk));
        dft_result.imag += (series[k].imag * cos(n * tk) - series[k].real * sin(n * tk));
    }
    return dft_result;                                          //Outputs a singular complex number corresponding to the result
}


Complex ift(int num,int N, int k, double T){                    //Inverse fourier transform function for H1 and H2                                        
    Complex ift_result = {0,0};                                     
    if (num ==1 || num ==2){                                    //part f -> skips n=1 for H1 and n=0 for H2   
        for (int n = 0; n<N;n++){
            if((num==1 && n==1)||(num==2 && n==0)){            
                continue;
            }
            else{
                Complex dft_result = dft(num,N,n,T);
                ift_result.real += (dft_result.real * cos (n*T*k/N) - dft_result.imag * sin(n*T*k/N))/N;        //ift calculation
                ift_result.imag += (dft_result.real * sin (n*T*k/N) + dft_result.imag * cos(n*T*k/N))/N;
            }
        }
    }
    return ift_result;                                          //output is a singular complex number representing the result of the ift
}


void sort(Complex*h3_sort){                                                     //Sorting function for finding the 4 terms with the largest amplitude
    Complex val1 = {0,0},val2 = {0,0}, val3 = {0,0}, val4 = {0,0};
    Complex dft_result;
    for (int n=0;n<200;n++){
        dft_result = dft(3,200,n,2*PI);
        if(mag(dft_result) >= mag(val1)){                       //Checks if the magnitude is larger than the current largest magnitude 
            val4.real = val3.real;                              //If it is, it moves all the values down one and stored the new value in 1st slot
            val4.imag = val3.imag;
            val3.real = val2.real;
            val3.imag = val2.imag;
            val2.real = val1.real;
            val2.imag = val1.imag;
            val1.real = dft_result.real;
            val1.imag = dft_result.imag;
        }
        else if(mag(dft_result) >= mag(val2)){                  //Same logic, just applied to the 2nd, 3rd and 4th largest values
            val4.real = val3.real;
            val4.imag = val3.imag;
            val3.real = val2.real;
            val3.imag = val2.imag;
            val2.real = dft_result.real;
            val2.imag = dft_result.imag;
        }
        else if(mag(dft_result) >= mag(val3)){
            val4.real = val3.real;
            val4.imag = val3.imag;
            val3.real = dft_result.real;
            val3.imag = dft_result.imag;
        }
        else if(mag(dft_result) >= mag(val4)){
            val4.real = dft_result.real;
            val4.imag = dft_result.imag;
        }
    }                                                           
    h3_sort[0] = val1;                                          //Storing the values to an array to be outputted
    h3_sort[1] = val2;
    h3_sort[2] = val3;
    h3_sort[3] = val4;

}
Complex ift3(int num,int N, int k, double T, Complex sorted[]){         //Seperate ift function for H3. Takes the sorted values as an argument 
    Complex ift_result = {0,0} ;
    for (int n=0;n<N;n++){  
        Complex dft_result = dft(num,N,n,T);                      
        if (isequal(dft_result,sorted[0])||isequal(dft_result,sorted[1])||isequal(dft_result,sorted[2])||isequal(dft_result,sorted[3])){    //The ift is only performed if the value for H3 is equal to one of the highest values previously sorted.
            ift_result.real += (dft_result.real * cos (n*T*k/N) - dft_result.imag * sin(n*T*k/N))/N;
            ift_result.imag += (dft_result.real * sin (n*T*k/N) + dft_result.imag * cos(n*T*k/N))/N;
        }
        else{
            continue;               //Skips the calculationwhen not one of the highest values
        }
    }
    return ift_result;              //Returns a singular complex struct
}

int main(){                                        
    FILE *fp1;                                                          //Opening a file for h1 values
    fp1 = fopen("h1.txt", "w");
    Complex h1_result[100];
    h1(100,2*PI,h1_result);                                             //h1 returns an array via a pointer so I first define the array the put it in the function argument
    for (int k=0; k<100; k++)
    {   
        fprintf(fp1, "%f , %f, %d\n", h1_result[k].real,h1_result[k].imag,k);           //Printing each value of the array into the file
    }
    fclose(fp1);

    printf("H1 values\n");                                            //Printing the values of H1 for all 100 values of n
    for (int n=0;n<100;n++){
        Complex h1_dft = dft(1,100,n,2*PI);
        printf("n = %d ->%f + i%f\n",n,h1_dft.real,h1_dft.imag);
    }
    
    FILE *fp1i;
    fp1i = fopen("h1_ift.txt", "w");                                        //Creating a file for ift of H1
    for (int k=0; k<100; k++){                                                                   
        Complex ift_result = ift(1,100,k,2*PI);                             //ift function only returns one complex number, so I include the function call inside the loop this time
        fprintf(fp1i, "%f , %f, %d\n", ift_result.real,ift_result.imag,k);
    }
    fclose(fp1i);
 
    FILE *fp2; 
    fp2 = fopen("h2.txt", "w");                                             //Repeating file writing for h2
    Complex h2_result[100];
    h2(100,2*PI,h2_result);
    for (int k=0; k<100; k++){   
        fprintf(fp2, "%f , %f, %d\n", h2_result[k].real,h2_result[k].imag,k);
    }
    fclose(fp2);

    printf("\nH2 values\n");
    for (int n=0;n<100;n++){                                            //Printing values of H2 for all 100 values of n
        Complex h2_dft = dft(2,100,n,2*PI);
        printf("n = %d ->%f + i%f\n",n,h2_dft.real,h2_dft.imag);
    }
    
    FILE *fp2i;                                                             //Repeating ift file writing for h2
    fp2i = fopen("h2_ift", "w");
    for (int k=0; k<100; k++){   
        Complex ift_result = ift(2,100,k,2*PI);
        fprintf(fp2i, "%f , %f, %d\n", ift_result.real,ift_result.imag,k);
    }
    fclose(fp2i);

    
    Complex sorted[4];                                                      //File writing for h3 ift
    sort(sorted);                                                           //I call the sorted function first so that i can pass in the array into the ift function
    FILE *fp3i;
    fp3i = fopen("h3_ift", "w");
    for (int k=0; k<100; k++){   
        Complex ift_result = ift3(3,100,k,2*PI,sorted);
        fprintf(fp3i, "%f , %f, %d\n", ift_result.real,ift_result.imag,k);
    }
    fclose(fp3i);
    }