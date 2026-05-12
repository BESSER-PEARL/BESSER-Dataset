





import java.util.List;
import java.util.ArrayList;

public class savingAccount  {

    private String annualGain;
    private String extraFee;
    private String annualInterestRate;



    public savingAccount(
        String annualGain,        String extraFee,        String annualInterestRate    ) {
        this.annualGain = annualGain;
        this.extraFee = extraFee;
        this.annualInterestRate = annualInterestRate;
    }


    public String getAnnualgain() {
        return annualGain;
    }

    public void setAnnualgain(String annualGain) {
        this.annualGain = annualGain;
    }
    public String getExtrafee() {
        return extraFee;
    }

    public void setExtrafee(String extraFee) {
        this.extraFee = extraFee;
    }
    public String getAnnualinterestrate() {
        return annualInterestRate;
    }

    public void setAnnualinterestrate(String annualInterestRate) {
        this.annualInterestRate = annualInterestRate;
    }


}