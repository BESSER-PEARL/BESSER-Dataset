





import java.util.List;
import java.util.ArrayList;

public class gama_EVariable  {

    private String error;
    private String max;
    private String function;
    private String name;
    private String min;
    private String type;
    private String update;
    private String hasError;
    private String init;



    public gama_EVariable(
        String error,        String max,        String function,        String name,        String min,        String type,        String update,        String hasError,        String init    ) {
        this.error = error;
        this.max = max;
        this.function = function;
        this.name = name;
        this.min = min;
        this.type = type;
        this.update = update;
        this.hasError = hasError;
        this.init = init;
    }


    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }
    public String getHaserror() {
        return hasError;
    }

    public void setHaserror(String hasError) {
        this.hasError = hasError;
    }
    public String getInit() {
        return init;
    }

    public void setInit(String init) {
        this.init = init;
    }


}