





import java.util.List;
import java.util.ArrayList;

public class ArduinoMetamodel_Pin  {

    private String label;
    private String pinMode;



    public ArduinoMetamodel_Pin(
        String label,        String pinMode    ) {
        this.label = label;
        this.pinMode = pinMode;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getPinmode() {
        return pinMode;
    }

    public void setPinmode(String pinMode) {
        this.pinMode = pinMode;
    }


}