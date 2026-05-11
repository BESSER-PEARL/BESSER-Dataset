





import java.util.List;
import java.util.ArrayList;

public class afpText_SetBiLevelImageColor extends triplet {

    private String NAMECOLR;
    private String AREA;
    private String Reserved;



    public afpText_SetBiLevelImageColor(
        String NAMECOLR,        String AREA,        String Reserved    ) {
        super(
        );
        this.NAMECOLR = NAMECOLR;
        this.AREA = AREA;
        this.Reserved = Reserved;
    }


    public String getNamecolr() {
        return NAMECOLR;
    }

    public void setNamecolr(String NAMECOLR) {
        this.NAMECOLR = NAMECOLR;
    }
    public String getArea() {
        return AREA;
    }

    public void setArea(String AREA) {
        this.AREA = AREA;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }


}