# SSH With Priveledged Account Alias

Many enterprise encorce policy that admins should use a separate, usually elevated/priveledged, account to access sensitive or critical systems.

I've found that creating an alias to ssh into hosts that require eleveated access to be one of the best timesavers I've ever had.  

So, if my priv account was `Doug.E.Doug-administrator-overlord`, that's a lot of typing I'd have to do to get into a box....which I have to do A LOT.  And with a low idle timeout, that just makes it a real pain in the ass.

## Solution:  Linux Alias

```bash
> echo alias ssha='ssh -l Doug.E.Doug-administrator-overlord ' >> ~/.bashrc

> source ~/.bashrc
```


Now all i have to do is type `ssha sekretserver` to get into my box using my admin account
