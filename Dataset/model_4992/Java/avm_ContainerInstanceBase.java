





import java.util.List;
import java.util.ArrayList;

public class avm_ContainerInstanceBase  {

    private String XPosition;
    private String IDinSourceModel;
    private String YPosition;



    public avm_ContainerInstanceBase(
        String XPosition,        String IDinSourceModel,        String YPosition    ) {
        this.XPosition = XPosition;
        this.IDinSourceModel = IDinSourceModel;
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
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }


}