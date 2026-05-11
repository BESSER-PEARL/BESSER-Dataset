





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_InvokeTransformation extends Expression {

    private String entryPointName;
    private String transformationName;



    public frontend_qool_InvokeTransformation(
        String entryPointName,        String transformationName    ) {
        super(
        );
        this.entryPointName = entryPointName;
        this.transformationName = transformationName;
    }


    public String getEntrypointname() {
        return entryPointName;
    }

    public void setEntrypointname(String entryPointName) {
        this.entryPointName = entryPointName;
    }
    public String getTransformationname() {
        return transformationName;
    }

    public void setTransformationname(String transformationName) {
        this.transformationName = transformationName;
    }


}