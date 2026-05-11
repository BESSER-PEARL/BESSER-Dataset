





import java.util.List;
import java.util.ArrayList;

public class filetree_Container extends FileTreeElement {






    private List<filetree_FileTreeElement> filetree_filetreeelements;




    private filetree_FileTreeElement filetree_filetreeelement;


    public filetree_Container(
    ) {
        super(
        );
        this.filetree_filetreeelements = new ArrayList<>();
    }

    public filetree_Container(
        ArrayList<filetree_FileTreeElement> filetree_filetreeelements    ) {
        this.filetree_filetreeelements = filetree_filetreeelements;
    }


    public List<filetree_FileTreeElement> getFiletree_filetreeelements() {
        return filetree_filetreeelements;
    }

    public void addFiletree_filetreeelement(Filetree_filetreeelement filetree_filetreeelement) {
        this.filetree_filetreeelements.add(filetree_filetreeelement);
    }
    public filetree_FileTreeElement getFiletree_filetreeelement() {
        return filetree_filetreeelement;
    }

    public void setFiletree_filetreeelement(filetree_FileTreeElement filetree_filetreeelement) {
        this.filetree_filetreeelement = filetree_filetreeelement;
    }

}