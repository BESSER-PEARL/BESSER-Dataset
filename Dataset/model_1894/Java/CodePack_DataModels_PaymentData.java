





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_PaymentData  {

    private int id;
    private String cc_number;
    private int cc_month;
    private String cc_first_name;
    private String cc_last_name;
    private int cc_year;
    private String cc_ccv;



    public CodePack_DataModels_PaymentData(
        int id,        String cc_number,        int cc_month,        String cc_first_name,        String cc_last_name,        int cc_year,        String cc_ccv    ) {
        this.id = id;
        this.cc_number = cc_number;
        this.cc_month = cc_month;
        this.cc_first_name = cc_first_name;
        this.cc_last_name = cc_last_name;
        this.cc_year = cc_year;
        this.cc_ccv = cc_ccv;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCc_number() {
        return cc_number;
    }

    public void setCc_number(String cc_number) {
        this.cc_number = cc_number;
    }
    public int getCc_month() {
        return cc_month;
    }

    public void setCc_month(int cc_month) {
        this.cc_month = cc_month;
    }
    public String getCc_first_name() {
        return cc_first_name;
    }

    public void setCc_first_name(String cc_first_name) {
        this.cc_first_name = cc_first_name;
    }
    public String getCc_last_name() {
        return cc_last_name;
    }

    public void setCc_last_name(String cc_last_name) {
        this.cc_last_name = cc_last_name;
    }
    public int getCc_year() {
        return cc_year;
    }

    public void setCc_year(int cc_year) {
        this.cc_year = cc_year;
    }
    public String getCc_ccv() {
        return cc_ccv;
    }

    public void setCc_ccv(String cc_ccv) {
        this.cc_ccv = cc_ccv;
    }


}