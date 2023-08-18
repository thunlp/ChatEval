如果在执行`conda install pip`后，`which pip`仍然没有显示Conda环境的路径，可能是由于某种原因，系统的`PATH`变量中Conda的路径没有得到优先考虑。以下是一些建议的解决方法：

1. **确保Conda环境已激活**：在尝试任何其他解决方案之前，请确保你的Conda环境确实已经被激活。你可以用以下命令来激活：
   ```bash
   conda activate your_env_name
   ```

2. **查看你的PATH**：运行以下命令，检查输出：
   ```bash
   echo $PATH
   ```
   你应该能够在输出中看到Conda环境的路径，类似于`/path/to/conda/envs/your_env_name/bin`。确保这个路径在其他可能包含`pip`的路径之前。

3. **手动指定pip的路径**：你可以直接使用完整路径来运行Conda环境中的pip，如下所示：
   ```bash
   /path/to/conda/envs/your_env_name/bin/pip install package_name
   ```

4. **调整PATH变量**：你可以临时地修改`PATH`变量，将Conda环境的`bin`目录放在最前面：
   ```bash
   export PATH="/path/to/conda/envs/your_env_name/bin:$PATH"
   ```

5. **检查.bashrc或.zshrc**：有时，你的`.bashrc`、`.bash_profile`或`.zshrc`（取决于你使用的shell）可能包含修改`PATH`的行，这可能会影响Conda环境的行为。确保没有其他软件或配置干扰了你的`PATH`设置。

6. **重安装Conda环境**：作为最后的手段，你可以考虑重新创建你的Conda环境。这通常可以确保所有组件都按预期安装和配置。

```bash
conda create -n new_env_name python=your_desired_version
conda activate new_env_name
conda install pip
which pip
```

希望上述方法之一可以帮助你解决问题。