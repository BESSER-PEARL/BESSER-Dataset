





import java.util.List;
import java.util.ArrayList;

public class room_ExternalType extends ComplexType {

    private String targetName;



    public room_ExternalType(
        String targetName    ) {
        super(
        );
        this.targetName = targetName;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }


}