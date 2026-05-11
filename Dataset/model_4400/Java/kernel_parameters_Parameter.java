





import java.util.List;
import java.util.ArrayList;

public class kernel_parameters_Parameter extends DataItem {

    private String correspondingArgument;
    private boolean byReference;



    public kernel_parameters_Parameter(
        String correspondingArgument,        boolean byReference    ) {
        super(
        );
        this.correspondingArgument = correspondingArgument;
        this.byReference = byReference;
    }


    public String getCorrespondingargument() {
        return correspondingArgument;
    }

    public void setCorrespondingargument(String correspondingArgument) {
        this.correspondingArgument = correspondingArgument;
    }
    public boolean getByreference() {
        return byReference;
    }

    public void setByreference(boolean byReference) {
        this.byReference = byReference;
    }


}