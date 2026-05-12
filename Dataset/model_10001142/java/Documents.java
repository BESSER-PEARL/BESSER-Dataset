





import java.util.List;
import java.util.ArrayList;

public class Documents  {

    private None data;
    private String file;
    private String file_name;
    private int tab_counter;



    public Documents(
        None data,        String file,        String file_name,        int tab_counter    ) {
        this.data = data;
        this.file = file;
        this.file_name = file_name;
        this.tab_counter = tab_counter;
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
    public String getFile_name() {
        return file_name;
    }

    public void setFile_name(String file_name) {
        this.file_name = file_name;
    }
    public int getTab_counter() {
        return tab_counter;
    }

    public void setTab_counter(int tab_counter) {
        this.tab_counter = tab_counter;
    }


}