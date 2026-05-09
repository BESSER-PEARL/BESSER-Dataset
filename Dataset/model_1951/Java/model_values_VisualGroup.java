





import java.util.List;
import java.util.ArrayList;

public class model_values_VisualGroup extends Node {

    private String highSpectrumColor;
    private String lowSpectrumColor;
    private String type;



    public model_values_VisualGroup(
        String highSpectrumColor,        String lowSpectrumColor,        String type    ) {
        super(
        );
        this.highSpectrumColor = highSpectrumColor;
        this.lowSpectrumColor = lowSpectrumColor;
        this.type = type;
    }


    public String getHighspectrumcolor() {
        return highSpectrumColor;
    }

    public void setHighspectrumcolor(String highSpectrumColor) {
        this.highSpectrumColor = highSpectrumColor;
    }
    public String getLowspectrumcolor() {
        return lowSpectrumColor;
    }

    public void setLowspectrumcolor(String lowSpectrumColor) {
        this.lowSpectrumColor = lowSpectrumColor;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}