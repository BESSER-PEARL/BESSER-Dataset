





import java.util.List;
import java.util.ArrayList;

public class component_PortSynchronizer extends IPropertyMap {

    private String originalPortString;



    public component_PortSynchronizer(
        String originalPortString    ) {
        super(
        );
        this.originalPortString = originalPortString;
    }


    public String getOriginalportstring() {
        return originalPortString;
    }

    public void setOriginalportstring(String originalPortString) {
        this.originalPortString = originalPortString;
    }


}