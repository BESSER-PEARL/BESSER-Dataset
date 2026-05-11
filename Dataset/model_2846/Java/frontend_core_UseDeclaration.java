





import java.util.List;
import java.util.ArrayList;

public class frontend_core_UseDeclaration extends RepresentModel {

    private String as_;
    private String module;



    public frontend_core_UseDeclaration(
        String as_,        String module    ) {
        super(
        );
        this.as_ = as_;
        this.module = module;
    }


    public String getAs_() {
        return as_;
    }

    public void setAs_(String as_) {
        this.as_ = as_;
    }
    public String getModule() {
        return module;
    }

    public void setModule(String module) {
        this.module = module;
    }


}