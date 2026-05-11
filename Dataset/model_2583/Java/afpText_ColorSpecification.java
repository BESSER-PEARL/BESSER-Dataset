





import java.util.List;
import java.util.ArrayList;

public class afpText_ColorSpecification extends triplet {

    private String ColSize2;
    private String ColSpce;
    private String ColSize4;
    private String ColSize1;
    private String Color;
    private String ColSize3;



    public afpText_ColorSpecification(
        String ColSize2,        String ColSpce,        String ColSize4,        String ColSize1,        String Color,        String ColSize3    ) {
        super(
        );
        this.ColSize2 = ColSize2;
        this.ColSpce = ColSpce;
        this.ColSize4 = ColSize4;
        this.ColSize1 = ColSize1;
        this.Color = Color;
        this.ColSize3 = ColSize3;
    }


    public String getColsize2() {
        return ColSize2;
    }

    public void setColsize2(String ColSize2) {
        this.ColSize2 = ColSize2;
    }
    public String getColspce() {
        return ColSpce;
    }

    public void setColspce(String ColSpce) {
        this.ColSpce = ColSpce;
    }
    public String getColsize4() {
        return ColSize4;
    }

    public void setColsize4(String ColSize4) {
        this.ColSize4 = ColSize4;
    }
    public String getColsize1() {
        return ColSize1;
    }

    public void setColsize1(String ColSize1) {
        this.ColSize1 = ColSize1;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getColsize3() {
        return ColSize3;
    }

    public void setColsize3(String ColSize3) {
        this.ColSize3 = ColSize3;
    }


}