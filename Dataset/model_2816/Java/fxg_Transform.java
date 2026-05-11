





import java.util.List;
import java.util.ArrayList;

public class fxg_Transform extends FXGElement {






    private fxg_Group fxg_group;




    private fxg_ColorTransform fxg_colortransform;




    private fxg_Matrix fxg_matrix;




    private fxg_Path fxg_path;


    public fxg_Transform(
    ) {
        super(
        );
    }



    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }
    public fxg_ColorTransform getFxg_colortransform() {
        return fxg_colortransform;
    }

    public void setFxg_colortransform(fxg_ColorTransform fxg_colortransform) {
        this.fxg_colortransform = fxg_colortransform;
    }
    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }
    public fxg_Path getFxg_path() {
        return fxg_path;
    }

    public void setFxg_path(fxg_Path fxg_path) {
        this.fxg_path = fxg_path;
    }

}