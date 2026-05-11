




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_LearningObject  {

    private boolean synchronized;
    private String id;
    private LocalDate timestamp;



    public lobj_LearningObject(
        boolean synchronized,        String id,        LocalDate timestamp    ) {
        this.synchronized = synchronized;
        this.id = id;
        this.timestamp = timestamp;
    }


    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }


}