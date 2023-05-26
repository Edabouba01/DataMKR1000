class fiche
{
private:
    /* data */
public:
    fiche(/* args */);
    ~fiche();
    // Pour SEN0307
#define MAX_RANG (520)        // the max measurement vaule of the module is 520cm(a little bit longer than  effective max range)
#define ADC_SOLUTION (1023.0) // ADC accuracy of Arduino UNO is 10bit

    int sensityPin = A0; // select the input pin

    float dist_t, sensity_t;

    // Broche du capteur
    int Sen0017=A0;
    int sensorPin = 3;
    int SonPin = A1;
    int MouvPin = 2;
    int LedRedPin = 5;
    int LedRPin = 7;
    int LedVertPin = 6;
    void Renvoi();
    void requete();
};

