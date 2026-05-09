





import java.util.List;
import java.util.ArrayList;

public class model_values_VisualGroup extends Node {

    private String lowSpectrumColor;
    private String highSpectrumColor;
    private String type;



    public model_values_VisualGroup(
        String lowSpectrumColor,        String highSpectrumColor,        String type    ) {
        super(
        );
        this.lowSpectrumColor = lowSpectrumColor;
        this.highSpectrumColor = highSpectrumColor;
        this.type = type;
    }


    public String getLowspectrumcolor() {
        return lowSpectrumColor;
    }

    public void setLowspectrumcolor(String lowSpectrumColor) {
        this.lowSpectrumColor = lowSpectrumColor;
    }
    public String getHighspectrumcolor() {
        return highSpectrumColor;
    }

    public void setHighspectrumcolor(String highSpectrumColor) {
        this.highSpectrumColor = highSpectrumColor;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}