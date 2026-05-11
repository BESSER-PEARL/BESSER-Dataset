





import java.util.List;
import java.util.ArrayList;

public class becontent_Apply extends ApplyCommand {

    private String prefix;



    public becontent_Apply(
        String prefix    ) {
        super(
        );
        this.prefix = prefix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}