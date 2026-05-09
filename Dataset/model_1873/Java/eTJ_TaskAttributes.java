





import java.util.List;
import java.util.ArrayList;

public class eTJ_TaskAttributes extends ExportAttribute {

    private boolean all;
    private boolean booking;
    private boolean flags;
    private boolean responsible;
    private boolean maxend;
    private boolean depends;
    private boolean complete;
    private boolean minstart;
    private boolean maxstart;
    private boolean minend;
    private boolean none;
    private boolean priority;
    private boolean note;



    public eTJ_TaskAttributes(
        boolean all,        boolean booking,        boolean flags,        boolean responsible,        boolean maxend,        boolean depends,        boolean complete,        boolean minstart,        boolean maxstart,        boolean minend,        boolean none,        boolean priority,        boolean note    ) {
        super(
        );
        this.all = all;
        this.booking = booking;
        this.flags = flags;
        this.responsible = responsible;
        this.maxend = maxend;
        this.depends = depends;
        this.complete = complete;
        this.minstart = minstart;
        this.maxstart = maxstart;
        this.minend = minend;
        this.none = none;
        this.priority = priority;
        this.note = note;
    }


    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getBooking() {
        return booking;
    }

    public void setBooking(boolean booking) {
        this.booking = booking;
    }
    public boolean getFlags() {
        return flags;
    }

    public void setFlags(boolean flags) {
        this.flags = flags;
    }
    public boolean getResponsible() {
        return responsible;
    }

    public void setResponsible(boolean responsible) {
        this.responsible = responsible;
    }
    public boolean getMaxend() {
        return maxend;
    }

    public void setMaxend(boolean maxend) {
        this.maxend = maxend;
    }
    public boolean getDepends() {
        return depends;
    }

    public void setDepends(boolean depends) {
        this.depends = depends;
    }
    public boolean getComplete() {
        return complete;
    }

    public void setComplete(boolean complete) {
        this.complete = complete;
    }
    public boolean getMinstart() {
        return minstart;
    }

    public void setMinstart(boolean minstart) {
        this.minstart = minstart;
    }
    public boolean getMaxstart() {
        return maxstart;
    }

    public void setMaxstart(boolean maxstart) {
        this.maxstart = maxstart;
    }
    public boolean getMinend() {
        return minend;
    }

    public void setMinend(boolean minend) {
        this.minend = minend;
    }
    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getPriority() {
        return priority;
    }

    public void setPriority(boolean priority) {
        this.priority = priority;
    }
    public boolean getNote() {
        return note;
    }

    public void setNote(boolean note) {
        this.note = note;
    }


}