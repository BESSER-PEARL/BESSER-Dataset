





import java.util.List;
import java.util.ArrayList;

public class ric_Checkbox extends FormControl {

    private boolean checked;



    public ric_Checkbox(
        boolean checked    ) {
        super(
        );
        this.checked = checked;
    }


    public boolean getChecked() {
        return checked;
    }

    public void setChecked(boolean checked) {
        this.checked = checked;
    }


}