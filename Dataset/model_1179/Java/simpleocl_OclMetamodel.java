





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OclMetamodel extends OclModel {

    private String uri;





    private simpleocl_Module simpleocl_module;


    public simpleocl_OclMetamodel(
        String uri    ) {
        super(
        );
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public simpleocl_Module getSimpleocl_module() {
        return simpleocl_module;
    }

    public void setSimpleocl_module(simpleocl_Module simpleocl_module) {
        this.simpleocl_module = simpleocl_module;
    }

}