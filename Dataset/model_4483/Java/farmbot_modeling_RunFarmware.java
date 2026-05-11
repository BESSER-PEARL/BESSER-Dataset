





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_RunFarmware extends SequenceCommand {

    private String name;



    public farmbot_modeling_RunFarmware(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}