





import java.util.List;
import java.util.ArrayList;

public class model_task_Checkable extends UnicaseModelElement {

    private boolean checked;



    public model_task_Checkable(
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