





import java.util.List;
import java.util.ArrayList;

public class model_DoorsLink  {

    private String targetModule;
    private String targetObject;





    private model_DoorsObject model_doorsobject;




    private model_DoorsObject model_doorsobject;


    public model_DoorsLink(
        String targetModule,        String targetObject    ) {
        this.targetModule = targetModule;
        this.targetObject = targetObject;
    }


    public String getTargetmodule() {
        return targetModule;
    }

    public void setTargetmodule(String targetModule) {
        this.targetModule = targetModule;
    }
    public String getTargetobject() {
        return targetObject;
    }

    public void setTargetobject(String targetObject) {
        this.targetObject = targetObject;
    }

    public model_DoorsObject getModel_doorsobject() {
        return model_doorsobject;
    }

    public void setModel_doorsobject(model_DoorsObject model_doorsobject) {
        this.model_doorsobject = model_doorsobject;
    }
    public model_DoorsObject getModel_doorsobject() {
        return model_doorsobject;
    }

    public void setModel_doorsobject(model_DoorsObject model_doorsobject) {
        this.model_doorsobject = model_doorsobject;
    }

}