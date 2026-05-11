





import java.util.List;
import java.util.ArrayList;

public class Trmodel_Update extends Operation {

    private String newName;



    public Trmodel_Update(
        String newName    ) {
        super(
        );
        this.newName = newName;
    }


    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }


}