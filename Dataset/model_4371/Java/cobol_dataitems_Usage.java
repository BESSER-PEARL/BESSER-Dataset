





import java.util.List;
import java.util.ArrayList;

public class cobol_dataitems_Usage extends DataItemAttribute {

    private String usage;
    private boolean isNative;



    public cobol_dataitems_Usage(
        String usage,        boolean isNative    ) {
        super(
        );
        this.usage = usage;
        this.isNative = isNative;
    }


    public String getUsage() {
        return usage;
    }

    public void setUsage(String usage) {
        this.usage = usage;
    }
    public boolean getIsnative() {
        return isNative;
    }

    public void setIsnative(boolean isNative) {
        this.isNative = isNative;
    }


}