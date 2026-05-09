





import java.util.List;
import java.util.ArrayList;

public class oaam_library_MessageType extends library_ResourceProviderA, common_OaamBaseElementA, library_ResourceConsumerA {

    private int minLength;
    private int maxLength;
    private int alignment;



    public oaam_library_MessageType(
        int minLength,        int maxLength,        int alignment    ) {
        super(
        );
        this.minLength = minLength;
        this.maxLength = maxLength;
        this.alignment = alignment;
    }


    public int getMinlength() {
        return minLength;
    }

    public void setMinlength(int minLength) {
        this.minLength = minLength;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public int getAlignment() {
        return alignment;
    }

    public void setAlignment(int alignment) {
        this.alignment = alignment;
    }


}