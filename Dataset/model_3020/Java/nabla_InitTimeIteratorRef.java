





import java.util.List;
import java.util.ArrayList;

public class nabla_InitTimeIteratorRef extends TimeIteratorRef {

    private int value;



    public nabla_InitTimeIteratorRef(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}