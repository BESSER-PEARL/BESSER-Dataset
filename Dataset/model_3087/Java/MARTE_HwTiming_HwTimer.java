





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwTiming_HwTimer extends HwTimingResource {






    private NFP_DataSize nfp_datasize;




    private HwTiming_HwClock hwtiming_hwclock;




    private NFP_Natural nfp_natural;


    public MARTE_HwTiming_HwTimer(
    ) {
        super(
        );
    }



    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public HwTiming_HwClock getHwtiming_hwclock() {
        return hwtiming_hwclock;
    }

    public void setHwtiming_hwclock(HwTiming_HwClock hwtiming_hwclock) {
        this.hwtiming_hwclock = hwtiming_hwclock;
    }
    public NFP_Natural getNfp_natural() {
        return nfp_natural;
    }

    public void setNfp_natural(NFP_Natural nfp_natural) {
        this.nfp_natural = nfp_natural;
    }

}