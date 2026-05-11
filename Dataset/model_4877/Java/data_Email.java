





import java.util.List;
import java.util.ArrayList;

public class data_Email extends MetaInformation {

    private String adress;



    public data_Email(
        String adress    ) {
        super(
        );
        this.adress = adress;
    }


    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }


}