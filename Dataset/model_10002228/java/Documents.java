





import java.util.List;
import java.util.ArrayList;

public class Documents  {

    private String file_name;
    private None data;
    private String file;
    private int tab_counter;



    public Documents(
        String file_name,        None data,        String file,        int tab_counter    ) {
        this.file_name = file_name;
        this.data = data;
        this.file = file;
        this.tab_counter = tab_counter;
    }


    public String getFile_name() {
        return file_name;
    }

    public void setFile_name(String file_name) {
        this.file_name = file_name;
    }
    public None getData() {
        return data;
    }

    public void setData(None data) {
        this.data = data;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public int getTab_counter() {
        return tab_counter;
    }

    public void setTab_counter(int tab_counter) {
        this.tab_counter = tab_counter;
    }


}