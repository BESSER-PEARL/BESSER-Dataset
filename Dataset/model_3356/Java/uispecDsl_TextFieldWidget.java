





import java.util.List;
import java.util.ArrayList;

public class uispecDsl_TextFieldWidget extends Widget {

    private int length;



    public uispecDsl_TextFieldWidget(
        int length    ) {
        super(
        );
        this.length = length;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}