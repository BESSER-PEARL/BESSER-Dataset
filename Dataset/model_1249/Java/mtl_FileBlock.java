





import java.util.List;
import java.util.ArrayList;

public class mtl_FileBlock extends Block {

    private String openMode;



    public mtl_FileBlock(
        String openMode    ) {
        super(
        );
        this.openMode = openMode;
    }


    public String getOpenmode() {
        return openMode;
    }

    public void setOpenmode(String openMode) {
        this.openMode = openMode;
    }


}