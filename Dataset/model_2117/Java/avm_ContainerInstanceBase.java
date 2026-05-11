





import java.util.List;
import java.util.ArrayList;

public class avm_ContainerInstanceBase  {

    private String IDinSourceModel;
    private String YPosition;
    private String XPosition;



    public avm_ContainerInstanceBase(
        String IDinSourceModel,        String YPosition,        String XPosition    ) {
        this.IDinSourceModel = IDinSourceModel;
        this.YPosition = YPosition;
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
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }


}