





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Workspace  {






    private List<cellsheet_EStringToTokenEntry> cellsheet_estringtotokenentrys;


    public cellsheet_Workspace(
    ) {
        this.cellsheet_estringtotokenentrys = new ArrayList<>();
    }

    public cellsheet_Workspace(
        ArrayList<cellsheet_EStringToTokenEntry> cellsheet_estringtotokenentrys    ) {
        this.cellsheet_estringtotokenentrys = cellsheet_estringtotokenentrys;
    }


    public List<cellsheet_EStringToTokenEntry> getCellsheet_estringtotokenentrys() {
        return cellsheet_estringtotokenentrys;
    }

    public void addCellsheet_estringtotokenentry(Cellsheet_estringtotokenentry cellsheet_estringtotokenentry) {
        this.cellsheet_estringtotokenentrys.add(cellsheet_estringtotokenentry);
    }

}