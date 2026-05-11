





import java.util.List;
import java.util.ArrayList;

public class avm_ContainerInstanceBase  {

    private String YPosition;
    private String XPosition;
    private String IDinSourceModel;



    public avm_ContainerInstanceBase(
        String YPosition,        String XPosition,        String IDinSourceModel    ) {
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.IDinSourceModel = IDinSourceModel;
    }


    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getIdinsourcemodel() {
        return IDinSourceModel;
    }

    public void setIdinsourcemodel(String IDinSourceModel) {
        this.IDinSourceModel = IDinSourceModel;
    }


}