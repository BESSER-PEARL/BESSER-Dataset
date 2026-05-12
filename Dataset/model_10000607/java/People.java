





import java.util.List;
import java.util.ArrayList;

public class People  {

    private String Custumer_;
    private String name;
    private String Worker;



    public People(
        String Custumer_,        String name,        String Worker    ) {
        this.Custumer_ = Custumer_;
        this.name = name;
        this.Worker = Worker;
    }


    public String getCustumer_() {
        return Custumer_;
    }

    public void setCustumer_(String Custumer_) {
        this.Custumer_ = Custumer_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWorker() {
        return Worker;
    }

    public void setWorker(String Worker) {
        this.Worker = Worker;
    }


}