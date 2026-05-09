





import java.util.List;
import java.util.ArrayList;

public class Classes_Bills_BillsManager extends IBills {






    private IBookablesAccess ibookablesaccess;


    public Classes_Bills_BillsManager(
    ) {
        super(
        );
    }



    public IBookablesAccess getIbookablesaccess() {
        return ibookablesaccess;
    }

    public void setIbookablesaccess(IBookablesAccess ibookablesaccess) {
        this.ibookablesaccess = ibookablesaccess;
    }

}