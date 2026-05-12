





import java.util.List;
import java.util.ArrayList;

public class infoCompany  {

    private String addressCompany;
    private String nameCompany;
    private String showSafe;
    private String phoneCompany;
    private String describeCompany;
    private String dateUpdate;
    private int idCompany;
    private String dateEstablish;
    private String dateRegister;



    public infoCompany(
        String addressCompany,        String nameCompany,        String showSafe,        String phoneCompany,        String describeCompany,        String dateUpdate,        int idCompany,        String dateEstablish,        String dateRegister    ) {
        this.addressCompany = addressCompany;
        this.nameCompany = nameCompany;
        this.showSafe = showSafe;
        this.phoneCompany = phoneCompany;
        this.describeCompany = describeCompany;
        this.dateUpdate = dateUpdate;
        this.idCompany = idCompany;
        this.dateEstablish = dateEstablish;
        this.dateRegister = dateRegister;
    }


    public String getAddresscompany() {
        return addressCompany;
    }

    public void setAddresscompany(String addressCompany) {
        this.addressCompany = addressCompany;
    }
    public String getNamecompany() {
        return nameCompany;
    }

    public void setNamecompany(String nameCompany) {
        this.nameCompany = nameCompany;
    }
    public String getShowsafe() {
        return showSafe;
    }

    public void setShowsafe(String showSafe) {
        this.showSafe = showSafe;
    }
    public String getPhonecompany() {
        return phoneCompany;
    }

    public void setPhonecompany(String phoneCompany) {
        this.phoneCompany = phoneCompany;
    }
    public String getDescribecompany() {
        return describeCompany;
    }

    public void setDescribecompany(String describeCompany) {
        this.describeCompany = describeCompany;
    }
    public String getDateupdate() {
        return dateUpdate;
    }

    public void setDateupdate(String dateUpdate) {
        this.dateUpdate = dateUpdate;
    }
    public int getIdcompany() {
        return idCompany;
    }

    public void setIdcompany(int idCompany) {
        this.idCompany = idCompany;
    }
    public String getDateestablish() {
        return dateEstablish;
    }

    public void setDateestablish(String dateEstablish) {
        this.dateEstablish = dateEstablish;
    }
    public String getDateregister() {
        return dateRegister;
    }

    public void setDateregister(String dateRegister) {
        this.dateRegister = dateRegister;
    }


}