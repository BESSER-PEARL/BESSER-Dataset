





import java.util.List;
import java.util.ArrayList;

public class frontend_core_UseDeclaration extends RepresentModel {

    private String module;
    private String as_;



    public frontend_core_UseDeclaration(
        String module,        String as_    ) {
        super(
        );
        this.module = module;
        this.as_ = as_;
    }


    public String getModule() {
        return module;
    }

    public void setModule(String module) {
        this.module = module;
    }
    public String getAs_() {
        return as_;
    }

    public void setAs_(String as_) {
        this.as_ = as_;
    }


}