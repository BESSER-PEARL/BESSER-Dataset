





import java.util.List;
import java.util.ArrayList;

public class minidrone_Jump extends Instruction {

    private String jumpType;



    public minidrone_Jump(
        String jumpType    ) {
        super(
        );
        this.jumpType = jumpType;
    }


    public String getJumptype() {
        return jumpType;
    }

    public void setJumptype(String jumpType) {
        this.jumpType = jumpType;
    }


}