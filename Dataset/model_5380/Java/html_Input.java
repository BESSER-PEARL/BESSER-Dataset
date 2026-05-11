





import java.util.List;
import java.util.ArrayList;

public class html_Input extends Editable {

    private int maxLength;
    private String type;
    private int step;
    private int max;
    private boolean checked;
    private int min;



    public html_Input(
        int maxLength,        String type,        int step,        int max,        boolean checked,        int min    ) {
        super(
        );
        this.maxLength = maxLength;
        this.type = type;
        this.step = step;
        this.max = max;
        this.checked = checked;
        this.min = min;
    }


    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getStep() {
        return step;
    }

    public void setStep(int step) {
        this.step = step;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public boolean getChecked() {
        return checked;
    }

    public void setChecked(boolean checked) {
        this.checked = checked;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }


}