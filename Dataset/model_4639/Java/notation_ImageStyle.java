





import java.util.List;
import java.util.ArrayList;

public class notation_ImageStyle extends Style {

    private String antiAlias;
    private String maintainAspectRatio;



    public notation_ImageStyle(
        String antiAlias,        String maintainAspectRatio    ) {
        super(
        );
        this.antiAlias = antiAlias;
        this.maintainAspectRatio = maintainAspectRatio;
    }


    public String getAntialias() {
        return antiAlias;
    }

    public void setAntialias(String antiAlias) {
        this.antiAlias = antiAlias;
    }
    public String getMaintainaspectratio() {
        return maintainAspectRatio;
    }

    public void setMaintainaspectratio(String maintainAspectRatio) {
        this.maintainAspectRatio = maintainAspectRatio;
    }


}