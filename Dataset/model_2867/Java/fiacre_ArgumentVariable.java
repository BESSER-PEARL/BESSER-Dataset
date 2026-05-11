





import java.util.List;
import java.util.ArrayList;

public class fiacre_ArgumentVariable extends Variable {

    private boolean read;
    private boolean write;
    private boolean ref;



    public fiacre_ArgumentVariable(
        boolean read,        boolean write,        boolean ref    ) {
        super(
        );
        this.read = read;
        this.write = write;
        this.ref = ref;
    }


    public boolean getRead() {
        return read;
    }

    public void setRead(boolean read) {
        this.read = read;
    }
    public boolean getWrite() {
        return write;
    }

    public void setWrite(boolean write) {
        this.write = write;
    }
    public boolean getRef() {
        return ref;
    }

    public void setRef(boolean ref) {
        this.ref = ref;
    }


}