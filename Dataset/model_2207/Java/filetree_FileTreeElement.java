





import java.util.List;
import java.util.ArrayList;

public class filetree_FileTreeElement  {

    private String file;
    private String path;
    private String name;





    private filetree_PathToTreeElementMap filetree_pathtotreeelementmap;


    public filetree_FileTreeElement(
        String file,        String path,        String name    ) {
        this.file = file;
        this.path = path;
        this.name = name;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public filetree_PathToTreeElementMap getFiletree_pathtotreeelementmap() {
        return filetree_pathtotreeelementmap;
    }

    public void setFiletree_pathtotreeelementmap(filetree_PathToTreeElementMap filetree_pathtotreeelementmap) {
        this.filetree_pathtotreeelementmap = filetree_pathtotreeelementmap;
    }

}