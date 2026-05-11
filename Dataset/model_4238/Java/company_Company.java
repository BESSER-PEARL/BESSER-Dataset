





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private int numberOfManager;
    private String name;



    public company_Company(
        int numberOfManager,        String name    ) {
        this.numberOfManager = numberOfManager;
        this.name = name;
    }


    public int getNumberofmanager() {
        return numberOfManager;
    }

    public void setNumberofmanager(int numberOfManager) {
        this.numberOfManager = numberOfManager;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}