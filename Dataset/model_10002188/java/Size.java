





import java.util.List;
import java.util.ArrayList;

public class Size  {

    private int SizeID;
    private String SizeName;



    public Size(
        int SizeID,        String SizeName    ) {
        this.SizeID = SizeID;
        this.SizeName = SizeName;
    }


    public int getSizeid() {
        return SizeID;
    }

    public void setSizeid(int SizeID) {
        this.SizeID = SizeID;
    }
    public String getSizename() {
        return SizeName;
    }

    public void setSizename(String SizeName) {
        this.SizeName = SizeName;
    }


}