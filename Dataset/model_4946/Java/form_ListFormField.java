





import java.util.List;
import java.util.ArrayList;

public class form_ListFormField extends MultipleValuatedFormField {

    private int maxHeigth;



    public form_ListFormField(
        int maxHeigth    ) {
        super(
        );
        this.maxHeigth = maxHeigth;
    }


    public int getMaxheigth() {
        return maxHeigth;
    }

    public void setMaxheigth(int maxHeigth) {
        this.maxHeigth = maxHeigth;
    }


}