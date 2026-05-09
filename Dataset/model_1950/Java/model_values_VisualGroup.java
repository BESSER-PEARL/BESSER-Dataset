





import java.util.List;
import java.util.ArrayList;

public class model_values_VisualGroup extends Node {

    private String highSpectrumColor;
    private String type;
    private String lowSpectrumColor;



    public model_values_VisualGroup(
        String highSpectrumColor,        String type,        String lowSpectrumColor    ) {
        super(
        );
        this.highSpectrumColor = highSpectrumColor;
        this.type = type;
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
    public String getLowspectrumcolor() {
        return lowSpectrumColor;
    }

    public void setLowspectrumcolor(String lowSpectrumColor) {
        this.lowSpectrumColor = lowSpectrumColor;
    }


}