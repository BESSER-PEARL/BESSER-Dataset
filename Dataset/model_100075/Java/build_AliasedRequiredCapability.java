





import java.util.List;
import java.util.ArrayList;

public class build_AliasedRequiredCapability extends RequiredCapability {

    private String alias;



    public build_AliasedRequiredCapability(
        String alias    ) {
        super(
        );
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}