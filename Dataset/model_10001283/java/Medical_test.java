





import java.util.List;
import java.util.ArrayList;

public class Medical_test  {

    private String Date;
    private String Image;
    private String Lab;
    private String name;
    private int ID;





    private Diagnosis diagnosis;


    public Medical_test(
        String Date,        String Image,        String Lab,        String name,        int ID    ) {
        this.Date = Date;
        this.Image = Image;
        this.Lab = Lab;
        this.name = name;
        this.ID = ID;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getImage() {
        return Image;
    }

    public void setImage(String Image) {
        this.Image = Image;
    }
    public String getLab() {
        return Lab;
    }

    public void setLab(String Lab) {
        this.Lab = Lab;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Diagnosis getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(Diagnosis diagnosis) {
        this.diagnosis = diagnosis;
    }

}